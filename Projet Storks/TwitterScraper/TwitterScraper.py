import twint
import nest_asyncio
nest_asyncio.apply()

# Configure
c = twint.Config()
c.Search = "#Birth"
c.limit = 10
c.Store_json = True
c.Output = "data/#Birth2.json"


# Run
twint.run.Search(c)

import pandas as pd
pd.options.display.max_columns = 100
data = pd.read_json("data/#Birth2.json", lines=True)
data.shape
data.head()