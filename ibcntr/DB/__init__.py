import datetime
import pprint
from xmlrpc.client import Boolean
from ibcntr.auth import get_user_byId
import redis

pp = pprint.pp

class rData():
    def __init__(self, logger, url):
        self.logger = logger
        print('initializing..', url)
        self.r = redis.from_url(url, socket_timeout=60)
        self.get_bats()
 
    def _get_hash_id_by_id(self, id: str):
        """ 
        Возвращает ключ(хэш) для записи с id (имя ИБ)
        """
        hashes = self.r.keys(pattern="bat:*")
        result = None
        for hash_id in hashes:
            bat = self.r.hget(hash_id, 'id')
            if bat is None: break
            bat = bat if type(bat)==str else bat.decode('utf-8')
            if bat == id:
                result = hash_id
        self.logger.debug(f"for bat {id} got hash_id {result}")
        return result

    def log_ib_loading(self, bat):
        """
        Записывает дату последней загрузки в ИБ
        """
        from datetime import datetime
        value_to_set = datetime.now().isoformat()
        hash_id = self._get_hash_id_by_id(bat)
        if not hash_id is None:
            self.r.hset(hash_id, key="loaded_times", value=value_to_set)
        else:
            self.logger.error(f'hash not found for bat "{bat}"')

    def switch(self, bat, on, remote, userid):
        """
        Переключает статус батника bat
        """
        value_to_set = "on" if on else "off"
        hash_id = self._get_hash_id_by_id(bat)
        user = get_user_byId(userid)
        if not hash_id is None:
            # self.r.hmset(hash_id, {
            self.r.hset(hash_id, key="load", value=value_to_set) 
            self.r.hset(hash_id, key="changed", value=datetime.datetime.now().isoformat())
            self.r.hset(hash_id, key="changedby", value=f'{user.name} ({remote})')
            # self.logger.debug(f'bat {bat} state changed to {value_to_set.upper()} by {remote}')
        else:
            # self.logger.error(f"Hash for {bat} not found")
            raise Exception(f"Hash for {bat} not found")

    def rquery(self, bat):
        """
        Возвращает статус батника bat
        """
        hash_id = self._get_hash_id_by_id(bat)
        if hash_id is None:
            print(f'bat {bat} got None hash')
            return "NO_KEY_FOUND"
        load = self.r.hget(hash_id, "load")
        if load is None: 
            print(f'hash "{hash_id}" returns _None_ in "load" key')
            return "NO_KEY_FOUND"
        load = load if type(load)==str else load.decode('utf-8')
        # self.logger.debug(f"got 'load' key for {bat} = {load}")
        return load

    def get_bats(self):
        """
        Получает слепок базы данных в виде словаря словарей
        """

        hashes = self.r.keys(pattern="bat:*")

        keynames = [
            "id",
            "bat",
            "load",
            "name",
            "changed",
            "changedby",
            "loaded_times"
     ]
        self.bats = {}

        for hash_id in hashes:
            hash_id = hash_id
            res = self.r.hmget(hash_id, keynames)
            #print(f'HASH: {hash_id} RES: {res}')
            d = {};i = 0
            for _ in keynames:
                val = res[i]
                if val is None: break
                value = val if type(val)==str else val.decode('utf-8')
                d.update({keynames[i] : val})
                i += 1
            if not d == {}:
                # self.logger.debug(f'update "bats" with {d}:({type(d)})')
                self.bats.update({hash_id:d})

    def _init_db(self):
        """
        первоначальное заполнение базы данных.
        для настройки тестовой БД
        никогда не будет использоваться в продуктиве
        """
        from ibcntr.mock import redis_mock as ibs
        self.r.flushdb()

        with self.r.pipeline() as pipe:
            for i_id, bat in ibs.items():
                pipe.hmset(i_id, bat)
            pipe.execute()
        self.r.bgsave()

  

