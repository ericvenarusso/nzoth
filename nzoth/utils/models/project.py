from typing import Dict, Optional

from pydantic import BaseModel, StrictStr


class Project(BaseModel):
    name: StrictStr
    version: StrictStr
    description: Optional[StrictStr] = "A machine learning project"
    dependencies: Dict[str, str]
