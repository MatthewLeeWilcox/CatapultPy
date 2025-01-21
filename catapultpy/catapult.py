import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# Enable automatic conversion between R and pandas
# pandas2ri.activate()


# # Load the catapultR package
# catapultR = importr("catapultR")

# class CatapultAPI:
#     def __init__(self, token: str):
#         self.token = token
#         ro.r(f'api_token <- "{self.token}"')  # Store token in R

#     def get_sessions(self):
#         """Fetch session data from the Catapult API."""
#         ro.r('''

#             get_sessions <- function() {
#                 return(ofGetSessions(api_token))
#             }
#         ''')
#         get_sessions = ro.r["get_sessions"]
#         return pandas2ri.rpy2py(get_sessions())


#     def get_players(self):
#         """Fetch player data from the Catapult API."""
#         ro.r('''
#             get_players <- function() {
#                 return(ofGetPlayers(api_token))
#             }
#         ''')
#         get_players = ro.r["get_players"]
#         return pandas2ri.rpy2py(get_players())

# # Example usage:
# # api = CatapultAPI("your_api_token")
# # print(api.get_sessions())
