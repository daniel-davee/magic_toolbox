from typing import Any
from pysimplelog import Logger

logger = Logger(__name__)
logger.set_log_file_basename(__name__)
logger.set_minimum_level(logger.logLevels['info'])
class Magic_dict(dict):
   
    _pure = False
    
    def __init__(self,obj:Any=None):
        self._obj = obj if obj else obj
        if isinstance(obj,dict): super().__init__(self._obj)
        else:super().__init__({})
        debug_questions = f"""What is obj?
                              {obj=}
                              what is bool(obj)?
                              {bool(obj)}
                              """
        logger.debug(debug_questions)
    
    def __call__(self,*args, **kwargs) -> Any:
        return self._obj(*args,**kwargs) if callable(self._obj) else self._obj
    
    def __getattr__(self, key):
        return self[key]
    
    def __getitem__(self, key: str) -> Any:
        """[key is split into head and tail (everything else)
        if tail can be true in some sense call self[head] and 
        then try to call tail, if tail is empty and it already exist just return that,
        if it does exist yet don't worry, let's make magic_dict]

        Args:
            key (str): [key is in object path format, key1.key2.key3 or empty]]

        Returns:
            Any: [description]
        """
        if key not in self:
            super().__setitem__(key, Magic_dict())
        return super().__getitem__(key)
            
    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
            return
        raise AttributeError(key)

    def __repr__(self):
        return '<Magic_dict ' + dict.__repr__(self) + '>'
