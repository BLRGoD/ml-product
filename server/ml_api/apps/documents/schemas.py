from typing import List, Union, Dict, Any, Optional
from enum import Enum
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class TaskType(Enum):
    classification = 'classification'
    regression = 'regression'


class ColumnTypes(BaseModel):
    numeric: List[str]
    categorical: List[str]
    target: Optional[str] = None
    task_type: Optional[TaskType] = None


class ColumnDescription(BaseModel):
    name: str
    type: str
    not_null_count: int
    data_type: str
    data: List[Dict]


class DocumentDescription(BaseModel):
    count: Dict
    mean: Dict
    std: Dict
    min: Dict
    first_percentile: Dict
    second_percentile: Dict
    third_percentile: Dict
    max: Dict


class PipelineElement(BaseModel):
    function_name: str
    param: Union[str, int, float] = None


class DocumentFullInfo(BaseModel):
    id: UUID
    name: str
    upload_date: datetime
    change_date: datetime
    pipeline: List[PipelineElement]
    column_types: Optional[ColumnTypes]


class DocumentShortInfo(BaseModel):
    name: str
    upload_date: datetime
    change_date: datetime


class ReadDocumentResponse(BaseModel):
    total: int
    records: Dict[str, List]


class ServiceResponse(BaseModel):
    status_code: int
    content: Any


class AvailableFunctions(Enum):
    remove_duplicates = 'remove_duplicates'
    drop_na = 'drop_na'
    miss_insert_mean_mode = 'miss_insert_mean_mode'
    miss_linear_imputer = 'miss_linear_imputer'
    miss_knn_imputer = 'miss_knn_imputer'
    standardize_features = 'standardize_features'
    ordinal_encoding = 'ordinal_encoding'
    one_hot_encoding = 'one_hot_encoding'
    outliers_isolation_forest = 'outliers_isolation_forest'
    outliers_elliptic_envelope = 'outliers_elliptic_envelope'
    outliers_local_factor = 'outliers_local_factor'
    outliers_one_class_svm = 'outliers_one_class_svm'
    outliers_sgd_one_class_svm = 'outliers_sgd_one_class_svm'
    fs_select_percentile = 'fs_select_percentile'
    fs_select_k_best = 'fs_select_k_best'
    fs_select_fpr = 'fs_select_fpr'
    fs_select_fdr = 'fs_select_fdr'
    fs_select_fwe = 'fs_select_fwe'
    fs_select_rfe = 'fs_select_rfe'
    fs_select_from_model = 'fs_select_from_model'
    fs_select_pca = 'fs_select_pca'
