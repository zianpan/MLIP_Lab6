import pytest
import pandas as pd

@pytest.fixture
def housing_data_stub():
    return pd.Dataframe(
      {price	area	bedrooms	bathrooms	stories	mainroad	guestroom	basement	hotwaterheating	airconditioning	parking	prefarea	furnishingstatus}
    )
