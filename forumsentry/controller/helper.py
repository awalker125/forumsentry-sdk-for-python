import forumsentry.models.xml_policy as xml_policy
  
def housestark():
    return "winter is coming"

def create_xml_policy():
    xml_policy_object = xml_policy(name="test", description=None, idp_group=None, request_task_group=None, response_task_group=None)
    return xml_policy_object


