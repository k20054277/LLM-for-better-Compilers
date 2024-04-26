
import as
import conda.ycm.commands

# Define the as environment
as.init(conda_env='my_env', python='3.8')

# Import libraries from the as environment
import pandas as pd

# Print the version of pandas
print(pd.__version__)

# Run conda commands from the as environment
conda.ycm.commands.run('conda list')

# Close the as environment
as.exit()
