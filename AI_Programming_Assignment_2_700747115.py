neighbors_county_graph = {
    "Adair":["Scotland", "Schuyler", "Putnam", "Sullivan", "Linn", "Macon", "Knox"],
    "Andrew": ["Holt", "Nodaway", "Buchanan", "DeKalb", "Gentry"],
    "Atchison": ["Nodaway","Holt"],
    "Audrain": ["Randolph", "Monroe", "Ralls", "Pike", "Montgomery", "Callaway", "Boone"],
    "Barry":["Lawrence", "Stone", "McDonald", "Newton"],
    "Barton":["Vernon", "Cedar", "Dade", "Jasper"],
    "Bates":["Cass", "Henry", "Vernon", "St. Clair"],
    "Benton":["Camden","Henry", "Pettis", "Morgan", "Hickory", "St. Clair"],
    "Bollinger":["Perry", "Cape Girardeau", "Madison", "Wayne", "Stoddard"],
    "Boone":["Audrain","Howard", "Cooper", "Randolph", "Callaway", "Cole", "Moniteau"],
    "Buchanan": ["Andrew", "DeKalb", "Clinton", "Platte"],
    "Butler":["Stoddard", "Wayne", "Carter", "Ripley", "Dunklin"],
    "Caldwell":["Daviess","Clinton", "Ray", "Carroll", "Livingston", "Daviess"],
    "Callaway":["Audrain", "Montgomery", "Osage", "Cole", "Boone","Gasconade"],
    "Camden":["Hickory","Benton","Miller", "Morgan", "Pulaski", "Laclede", "Dallas"],
    "Cape Girardeau":["Perry", "Bollinger", "Stoddard", "Scott"],
    "Carroll":["Livingston", "Chariton", "Saline", "Lafayette", "Ray", "Caldwell"],
    "Carter":["Ripley", "Butler", "Wayne", "Shannon", "Reynolds","Oregon"],
    "Cass":["Johnson","Jackson", "Bates", "Henry"],
    "Cedar":["St. Clair", "Polk", "Dade", "Vernon"],
    "Chariton":["Livingston","Linn", "Macon", "Randolph", "Howard", "Saline", "Carroll"],
    "Christian":["Lawrence","Greene", "Webster", "Douglas", "Taney", "Stone"],
    "Clark":["Scotland", "Lewis", "Knox"],
    "Clay":["Clinton", "Platte", "Ray", "Jackson"],
    "Clinton":["Buchanan", "DeKalb", "Caldwell", "Ray","Platte","Clay"],
    "Cole":["Moniteau", "Miller", "Osage", "Callaway", "Boone"],
    "Cooper":["Howard", "Boone", "Moniteau", "Morgan", "Pettis", "Saline"],
    "Crawford":["Washington", "Franklin", "Phelps", "Dent", "Iron", "Gasconade"],
    "Dade":["Jasper","Cedar", "Polk", "Greene", "Lawrence", "Barton"],
    "Dallas":["Webster","Camden", "Laclede", "Polk", "Greene", "Hickory"],
    "Daviess": ["Gentry", "DeKalb", "Caldwell", "Grundy", "Harrison","Livingston"],
    "DeKalb": ["Gentry", "Daviess", "Caldwell", "Clinton", "Buchanan", "Andrew"],
    "Dent":["Crawford", "Phelps", "Shannon", "Texas", "Reynolds", "Iron"],
    "Douglas":["Taney","Wright", "Texas", "Howell", "Ozark", "Christian", "Webster"],
    "Dunklin":["Butler","Stoddard", "New Madrid", "Pemiscot"],
    "Franklin":["St. Charles","Washington","Gasconade", "Warren", "St. Louis", "Jefferson", "Crawford"],
    "Gasconade":["Callaway","Crawford","Franklin", "Warren", "Montgomery", "Osage", "Maries", "Phelps"],
    "Gentry": ["Andrew","Worth", "Harrison", "Daviess", "DeKalb", "Nodaway"],
    "Greene":["Polk", "Webster", "Christian", "Lawrence", "Dade", "Dallas"],
    "Grundy":["Harrison", "Mercer", "Sullivan", "Linn", "Livingston", "Daviess"],
    "Harrison": ["Mercer", "Grundy", "Daviess", "Gentry", "Worth"],
    "Henry":["Johnson","Pettis", "Benton", "St. Clair", "Bates", "Cass"],
    "Hickory":["Benton", "St. Clair", "Camden", "Polk", "Dallas"],
    "Holt": ["Atchison", "Nodaway", "Andrew"],
    "Howard":["Randolph", "Boone", "Cooper", "Saline", "Chariton"],
    "Howell":["Shannon", "Texas", "Douglas", "Oregon", "Ozark"],
    "Iron":["Wayne","Washington", "St. Francois", "Madison", "Reynolds", "Dent", "Crawford"],
    "Jackson":["Cass","Johnson","Clay", "Lafayette"],
    "Jasper":["Barton", "Dade", "Lawrence", "Newton"],
    "Jefferson":["St. Louis", "Franklin", "Washington", "Ste. Genevieve", "St. Francois"],
    "Johnson":["Jackson","Cass", "Henry", "Pettis", "Lafayette"],
    "Knox":["Scotland","Clark", "Lewis", "Shelby", "Adair", "Macon"],
    "Laclede":["Dallas", "Webster", "Wright", "Pulaski", "Camden", "Texas"],
    "Lafayette":["Jackson","Ray", "Carroll", "Saline", "Pettis", "Johnson"],
    "Lawrence":["Christian","Dade", "Greene", "Newton", "Stone", "Jasper", "Barry"],
    "Lewis":["Clark", "Knox", "Shelby", "Marion"],
    "Lincoln":["Pike", "St. Charles", "Warren", "Montgomery"],
    "Linn":["Chariton","Adair", "Macon", "Sullivan", "Grundy", "Livingston"],
    "Livingston":["Chariton","Grundy", "Linn", "Caldwell", "Daviess", "Carroll"],
    "McDonald":["Newton", "Barry"],
    "Macon":["Monroe", "Sullivan","Adair", "Knox", "Shelby", "Randolph", "Chariton", "Linn"],
    "Madison":["Perry","Wayne", "Bollinger", "St. Francois", "Iron"],
    "Maries":["Phelps", "Gasconade", "Osage", "Miller", "Pulaski"],
    "Marion":["Lewis", "Shelby", "Monroe", "Ralls"],
    "Mercer":["Putnam", "Sullivan", "Grundy", "Harrison"],
    "Miller":["Osage","Moniteau","Pulaski","Morgan", "Camden", "Maries", "Cole"],
    "Mississippi":["New Madrid", "Scott"],
    "Moniteau":["Boone","Morgan", "Miller", "Cole", "Cooper"],
    "Monroe":["Ralls", "Shelby", "Marion", "Randolph", "Audrain"],
    "Montgomery":["Audrain","Warren", "Lincoln", "Pike", "Callaway", "Gasconade","Osage"],
    "Morgan":["Cooper","Camden", "Miller", "Moniteau", "Benton", "Pettis"],
    "New Madrid":["Pemiscot","Dunklin","Mississippi", "Scott", "Stoddard"],
    "Newton":["Jasper", "Lawrence", "Barry", "McDonald"],
    "Nodaway": ["Atchison", "Holt", "Andrew", "Gentry", "Worth"],
    "Oregon":["Howell", "Shannon", "Carter", "Ripley"],
    "Osage":["Montgomery","Gasconade", "Maries", "Miller", "Cole", "Callaway"],
    "Ozark":["Douglas", "Howell", "Taney"],
    "Pemiscot":["Dunklin", "New Madrid"],
    "Perry":["St. Francois", "Ste. Genevieve", "Cape Girardeau", "Bollinger", "Madison"],  
    "Pettis": ["Morgan","Lafayette","Johnson", "Benton", "Henry", "Saline", "Cooper"],
    "Phelps": ["Maries", "Gasconade", "Crawford", "Dent", "Pulaski", "Texas"],
    "Pike": ["Lincoln", "Montgomery", "Audrain", "Ralls"],
    "Platte": ["Buchanan", "Clinton", "Clay"],
    "Polk": ["Cedar", "Hickory", "Dallas", "Dade", "Greene", "St. Clair"],
    "Pulaski": ["Phelps", "Maries", "Miller", "Laclede", "Camden", "Texas"],
    "Putnam": ["Mercer", "Schuyler", "Adair", "Sullivan"],
    "Ralls": ["Marion", "Monroe", "Pike", "Audrain"],
    "Randolph": ["Shelby","Audrain", "Howard", "Macon", "Boone", "Chariton", "Monroe"],
    "Ray": ["Caldwell", "Clinton", "Clay", "Lafayette", "Carroll", "Jackson"],
    "Reynolds": ["Shannon", "Dent", "Iron", "Wayne", "Carter"],
    "Ripley": ["Butler", "Carter", "Oregon"],
    "St. Charles": ["Lincoln", "Warren", "St. Louis", "Franklin"],
    "St. Clair": ["Vernon","Henry", "Benton", "Hickory", "Polk", "Cedar", "Bates"],
    "Ste. Genevieve": ["Perry", "St. Francois", "Jefferson"],
    "St. Francois": ["Jefferson","Perry", "Ste. Genevieve", "Madison", "Iron", "Washington"],
    "St. Louis": ["St. Charles", "Franklin", "Jefferson"],
    "Saline": ["Lafayette", "Pettis", "Cooper", "Howard", "Chariton", "Carroll"],
    "Schuyler": ["Putnam", "Adair", "Scotland"],
    "Scotland": ["Schuyler","Clark", "Adair", "Knox"],
    "Scott": ["Mississippi", "New Madrid", "Cape Girardeau","Stoddard"],
    "Shannon": ["Dent","Oregon", "Howell", "Reynolds", "Carter", "Texas"],
    "Shelby": ["Marion", "Knox", "Lewis", "Macon", "Monroe","Randolph"],
    "Stoddard": ["Scott", "Butler", "Dunklin", "New Madrid","Wayne", "Bollinger", "Cape Girardeau"],
    "Stone": ["Taney", "Christian", "Lawrence", "Barry"],
    "Sullivan": ["Putnam", "Adair", "Linn", "Grundy", "Mercer"],
    "Taney": ["Christian", "Douglas", "Ozark", "Stone"],
    "Texas": ["Douglas","Laclede", "Wright", "Howell", "Shannon", "Pulaski", "Phelps", "Dent"],
    "Vernon": ["Bates", "Cedar", "St. Clair", "Barton"],
    "Warren": ["Montgomery", "Lincoln", "St. Charles", "Franklin", "Gasconade"],
    "Washington": ["Crawford", "Franklin", "Jefferson", "Iron", "St. Francois"],
    "Wayne": ["Iron","Madison","Stoddard" ,"Butler" ,"Reynolds", "Bollinger", "Carter"],
    "Webster": ["Greene", "Christian", "Douglas", "Wright", "Laclede", "Dallas"],
    "Worth": ["Nodaway", "Gentry", "Harrison"],
    "Wright": ["Douglas", "Webster", "Texas", "Laclede"]    
}

colors = ['Red', 'Blue', 'Green','Yellow','White']

counties = ['Adair', 'Andrew', 'Atchison', 'Audrain', 'Barry', 'Barton', 'Bates', 'Benton', 'Bollinger', 'Boone', 
            'Buchanan', 'Butler', 'Caldwell', 'Callaway', 'Camden', 'Cape Girardeau', 'Carroll', 'Carter', 'Cass', 
            'Cedar', 'Chariton', 'Christian', 'Clark', 'Clay', 'Clinton', 'Cole', 'Cooper', 'Crawford', 'Dade',
            'Dallas', 'Daviess', 'DeKalb', 'Dent', 'Douglas', 'Dunklin', 'Franklin', 'Gasconade', 'Gentry', 
            'Greene', 'Grundy', 'Harrison', 'Henry', 'Hickory', 'Holt', 'Howard', 'Howell', 'Iron', 'Jackson', 
            'Jasper', 'Jefferson', 'Johnson', 'Knox', 'Laclede', 'Lafayette', 'Lawrence', 'Lewis', 'Lincoln', 
            'Linn', 'Livingston', 'McDonald', 'Macon', 'Madison', 'Maries', 'Marion', 'Mercer', 'Miller', 'Mississippi', 
            'Moniteau', 'Monroe', 'Montgomery', 'Morgan', 'New Madrid', 'Newton', 'Nodaway', 'Oregon', 'Osage', 'Ozark', 
            'Pemiscot', 'Perry', 'Pettis', 'Phelps', 'Pike', 'Platte', 'Polk', 'Pulaski', 'Putnam', 'Ralls', 'Randolph', 
            'Ray', 'Reynolds', 'Ripley', 'St. Charles', 'St. Clair', 'Ste. Genevieve', 'St. Francois', 'St. Louis',
            'Saline', 'Schuyler', 'Scotland', 'Scott', 'Shannon', 'Shelby', 'Stoddard', 'Stone', 
            'Sullivan', 'Taney', 'Texas', 'Vernon', 'Warren', 'Washington', 'Wayne', 'Webster', 'Worth', 'Wright']

# Create an empty list to store neighbor county pairs
neighbour_county = []

# Iterate through the dictionary to extract neighbor county pairs
for keys, item in neighbors_county_graph.items():
    for county in item:
        neighbor = []
        neighbor.extend([keys, county])
        neighbour_county.append(neighbor)

# Define a function to remove duplicate entries in a 2D list
def remove_duplicates_2d(lst_2d):
    seen = set()
    unique_list = []

    # Iterate through the 2D list
    for sub_list in lst_2d:
        # Convert each sub-list to a frozenset to make it hashable
        frozen_sub = frozenset(sub_list)

        # Check if the frozenset has been seen before (indicating a duplicate)
        if frozen_sub not in seen:
            # Convert the frozenset back to a list and add it to the unique list
            unique_list.append(list(frozen_sub))
            seen.add(frozen_sub)

    return unique_list

# Example usage:
my_2d_list = neighbour_county

# Call the function to remove duplicate neighbor county pairs
unique_list_of_neighbor = remove_duplicates_2d(my_2d_list)

# The result is unique pairs of neighboring countys in `unique_list_of_neighbor`

     

# Import all the required libraries
from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type
# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables
    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...

# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # variables to be constrained
        self.domains: Dict[V, List[D]] = domains # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

   # Check if the value assignment is consistent by checking all constraints
   # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
      for constraint in self.constraints[variable]:
        if not constraint.satisfied(assignment):
          return False
      return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
      # assignment is complete if every variable is assigned (our base case)
      if len(assignment) == len(self.variables):
        return assignment
      # get all variables in the CSP but not in the assignment
      unassigned: List[V] = [v for v in self.variables if v not in assignment]
      # get the every possible domain value of the first unassigned variable
      first: V = unassigned[0]
      for value in self.domains[first]:
        local_assignment = assignment.copy()
        local_assignment[first] = value
        # if we're still consistent, we recurse (continue)
        if self.consistent(first, local_assignment):
            result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
            # if we didn't find the result, we will end up backtracking
            if result is not None:
                return result
      return None

# Define a constraint for map coloring
class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
          return True
        # check the color assigned to place1 is not the same as the color assigned to place2
        return assignment[self.place1] != assignment[self.place2]

if __name__ == "__main__":
    # Define the list of U.S. countys and their possible colors
    variables: List[str] = counties
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = colors

    # Create a CSP instance
    csp: CSP[str, str] = CSP(variables, domains)

 # Add map coloring constraints based on neighbor information
    for neighbor_list in unique_list_of_neighbor:
      #print(neighbor_list[0], neighbor_list[1])
      csp.add_constraint(MapColoringConstraint(neighbor_list[0], neighbor_list[1]))

# Solve the CSP using backtracking search
solution: Optional[Dict[str, str]] = csp.backtracking_search()

# Print the solution if found, or indicate no solution
if solution is None:
    print("No solution found!")
else:
    # Convert the solution to a DataFrame for better visualization
    print(solution)
