import recastapi

def analysis(uuid = None):  
    """List analysis given uuid or all analyses.
    
    Args:
    uuid: analysis_id.
    
    Returns:
    JSON object containing all analyses retrieved.
    """
    
    single_analysis = '/{}'.format(uuid) if uuid else ''
    url = '{}{}'.format(recastapi.ENDPOINTS['ANALYSIS'], single_analysis)
    return recastapi.get(url)
