from Yukki import (ASS_CLI_1, ASS_CLI_2, ASSID1, ASSID2, ASSNAME1, ASSNAME2,
                    ASSUSERNAME1, ASSUSERNAME2)

                   
async def get_assistant_details(assistant: int):
    if int(assistant) == 1:
        x = ASSID1
        y = ASSNAME1
        z = ASSUSERNAME1
        a = ASS_CLI_1
    elif int(assistant) == 2:
        x = ASSID2
        y = ASSNAME2
        z = ASSUSERNAME2
        a = ASS_CLI_2
    
