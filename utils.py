# utils.py
from bson import ObjectId
from datetime import datetime
from typing import Optional, Dict, Any

def obj_to_id(doc: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not doc:
        return None
    d = dict(doc)
    # rename _id -> id (string)
    _id = d.pop("_id", None)
    d["id"] = str(_id) if _id is not None else None
    # ensure datetime serialization for ISO strings
    for k, v in d.items():
        if isinstance(v, datetime):
            d[k] = v.isoformat()
    return d
