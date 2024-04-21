import numpy as np

def stats(dataframe) :
    """Function shows informations about dataset - shape and data types.
    
    Args:
        Function takes pandas dataframe.
    
    """
    print('### Shape ###')
    print(f'Rows: {dataframe.shape[0]}')
    print(f'Columns: {dataframe.shape[1]}')
    print('\n')
    print('### Data Types ###')
    print(dataframe.dtypes)
    print('\n')

def miss_dupl(dataframe) :
    """Function shows information about missing values and duplicates in dataset.

    Args:
        Function takes pandas dataframe.

    """
    print('\n')
    print('### Missing Values ###')
    ndf = dataframe.isna().sum()
    print(ndf[ndf > 0])
    print('\n')
    print('### Duplicate Values ###')
    print(dataframe.duplicated().sum())
    print('\n')
    print('### Unique Values ###')
    print(dataframe.nunique().sum())

def columns_bsize(dataframe) :
    """ Function shows size of each column in bytes.
    
    Args:
        Function takes pandas dataframe.

    Return:
        Function returns ...
    
    """
    return [f'{x} --- {dataframe[x].nbytes} --- {dataframe[x].dtype}' for x in dataframe]

def change_to_int(dataframe, list) :
    """ Change given columns type to int16.
    
    Args:
        dataframe -> pandas dataframe;
        list -> list of columns that type is changed to int16.

    """
    for x in list:
        dataframe[x] = dataframe[x].astype('int16')

def drop_missing_five(dataframe) :
    """ Function that shows which column is in drop treshold of 5% missing values.
    
    Args:
        Function takes pandas dataframe.

    Return:
        Value returned as ... of columns below 5% missing values.
    
    """
    tresh = int(len(dataframe) * 0.05)
    return dataframe.columns[dataframe.isna().sum() <= tresh]

def dataset_IQR(col) :
    """ Calculate IQR for given column """
    return np.quantile(col, 0.75) - np.quantile(col, 0.25)

def lower_tresh(col):
   """ Calculate lower treshold """ 
   return np.quantile(col, 0.25) - (1.5 * dataset_IQR(col))

def upper_tresh(col) :
    """ Calculate upper treshold """
    return np.quantile(col, 0.75) + (1.5 * dataset_IQR(col))

def lower_treshholders(dataframe) :
    """Check how many outliners-lower we have for each column"""
    for x in dataframe.select_dtypes(include= 'number') :
        print(f'Column: {x}')
        print(f'Lower treshold {lower_tresh(dataframe[x])}')
        print(f'Ilosc wartosci ponizej dolnego outlinera: {dataframe[x][dataframe[x] < lower_tresh(dataframe[x])].count()}\n')

def upper_treshholders(dataframe) :
    """Check how many outliners-upper we have for each column"""
    for x in dataframe.select_dtypes(include= 'number') :
        print(f'Column: {x}')
        print(f'Upper treshold {upper_tresh(dataframe[x])}')
        print(f'Ilosc wartosci powyzej górnego outlinera: {dataframe[x][dataframe[x] > upper_tresh(dataframe[x])].count()}\n')

def remove_outliners(dataframe) :
    """Remove outliners for column with number type"""
    for x in dataframe.select_dtypes(include= 'number') :
        dataframe = dataframe[(dataframe[x] >= lower_tresh(dataframe[x])) & (dataframe[x] <= upper_tresh(dataframe[x]))]
    return dataframe

def weight_average(group, col) :
    """Return weight mean"""
    d = group[col]
    w = group['Circulations']
    return (d * w).sum() / w.sum()