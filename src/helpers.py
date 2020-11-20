def load_data():
    """Load data from raw text files into a DataFrame
    """
    import pandas as pd
    import json
    from dateutil.parser import parse
    
    # Load raw text
    with open('../src/prices.txt', 'r') as file:
        lines = [json.loads(line) for line in file.readlines()]
    with open('../src/decoder.txt', 'r') as file:
        decoder = json.load(file)        
    
    # Hacky formatting for DataFrame
    dates = [parse(date) for line in lines for date in line]
    data = [list(x.values())[0] for x in lines]
    
    # Make Dataframe and convert coin codes to names
    result = pd.DataFrame(data=data, index=dates)   
    result.columns = result.columns.map(decoder)
    
    return result