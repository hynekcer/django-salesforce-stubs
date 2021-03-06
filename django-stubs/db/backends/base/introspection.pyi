from collections import namedtuple
from typing import Any, Dict, List, Optional, Tuple
from django.db import models
from django.db.backends.utils import CursorWrapper

TableInfo = namedtuple('TableInfo', ['name', 'type'])

FieldInfo = namedtuple('FieldInfo', 'name type_code display_size internal_size precision scale null_ok default')

class BaseDatabaseIntrospection:
    data_types_reverse: Dict = ...
    connection: Any = ...
    def __init__(self, connection: Any) -> None: ...
    def get_field_type(self, data_type: Any, description: Any) -> str: ...
    def identifier_converter(self, name: str) -> str: ...
    def table_names(self, cursor: Optional[CursorWrapper] = ..., include_views: bool = ...) -> List[str]: ...
    def get_table_list(self, cursor: CursorWrapper) -> List[TableInfo]: ...
    def get_migratable_models(self) -> List[models.Model]: ...
    def django_table_names(self, only_existing: bool = ..., include_views: bool = ...) -> List[str]: ...
    def installed_models(self, tables: Any) -> List[models.Model]: ...
    def sequence_list(self) -> List[Dict[str, str]]: ...
    def get_sequences(self, cursor: CursorWrapper, table_name: str, table_fields: Any = ...) -> List[Dict[str, str]]: ...
    def get_key_columns(self, cursor: CursorWrapper, table_name: str) -> List[Tuple[str, str, str]]: ...
    def get_primary_key_column(self, cursor: CursorWrapper, table_name: str) -> Optional[str]: ...
    def get_constraints(self, cursor: CursorWrapper, table_name: str) -> Dict[str, Dict[str, Any]]: ...
