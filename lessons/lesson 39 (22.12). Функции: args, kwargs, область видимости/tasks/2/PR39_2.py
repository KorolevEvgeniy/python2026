def prepare_request(**kwargs):
    if "endpoint" not in kwargs:
        raise ValueError("endpoint is required")
    
    endpoint = kwargs["endpoint"]
#    params = kwargs.copy()
    def split_control_params(params_dict):
        control_defaults = {"timeout": 5, "retries": 3}
        
        control = {}
        control["timeout"] = params_dict.get("timeout", control_defaults["timeout"])
        control["retries"] = params_dict.get("retries", control_defaults["retries"])
        
        payload_keys = [
            key for key in params_dict.keys() 
            if key not in ["endpoint", "timeout", "retries"]
        ]
        payload = {key: params_dict[key] for key in payload_keys}
        
        return control, payload
    control, payload = split_control_params(params)
    
    result = {
        "endpoint": endpoint,
        "control": control,
        "payload": payload
    }
    
    return result
    allowed_keys = {"mode", "stack", "level"}
print(prepare_request(endpoint="/stats", data=[1, 2]))
print(prepare_request(endpoint="/sync", timeout=10, retries=0, mode="fast"))
