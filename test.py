from ttp import ttp
import json
import pandas as pd


with open("haproxy.cfg") as f:
    data_to_parse = f.read()

template_haproxy_cfg = """
<group name="FRONTEND_CFG">
    acl {{host}} {{hdr}} {{i}} {{site}}
    use_backend {{backends}} {{if}} {{host}}
</group>
<group name="BACKEND_CFG">
backend {{backends}}  
       server {{Name}} {{IP}} {{check}} {{port}} {{num}}
</group>

"""

def haproxy_cfg_parser(data_to_parse):
    ttp_template = template_haproxy_cfg

    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()

    # print result in JSON format
    results = parser.result(format='json')[0]
    #print(results)

    #converting str to json.
    result = json.loads(results)

    with open('data.json', 'w') as f:
        json.dump(result, f, indent=4)

    return(result)

parsed_haproxy_cfg_parser = haproxy_cfg_parser(data_to_parse)

#f = open('data.json')

#data = json.load(f)

with open('data.json', 'r') as jf:
    jsonFile = json.load(jf)
    print(type(jsonFile))
    data = json.dumps(jsonFile[0]['FRONTEND_CFG']), json.dumps(jsonFile[0]['BACKEND_CFG'])
    print(data)
    print(type(data))
    backend = jsonFile[0]['BACKEND_CFG']
    print(backend)
    frontend = jsonFile[0]['FRONTEND_CFG']
    print(frontend)
    print(type(backend))

    backend1 = pd.DataFrame(backend)
    #backend1.to_csv("backend.csv")
    frontend1 = pd.DataFrame(frontend)
    #frontend1.to_csv("frontend.csv")

    combined_df = pd.merge(backend1, frontend1, on="backends")

    # Eliminare colonne
    delcol = combined_df.drop(['check', 'num', 'port', 'hdr', 'host', 'i', 'if'], axis=1)
    delcol.to_csv("backend_frontend.csv", index=False)