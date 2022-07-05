import boto3

from multiprocessing import Pool



def main(offset):
    client = boto3.client('dynamodb')
    response = client.scan(
        TableName='bobo-pscase-test'
    )
    print(response['Count'])
    print(response['ScannedCount'])
    print(response['ResponseMetadata'])


    for i in range(10):
        response = client.put_item(
            TableName='bobo-pscase-test',
            Item={
                
                "id": {
                    "S": "mp" + str(offset) + "2932451" + str(i) + str(i*3)
                },
                "AmazonGenerated": {
                    "BOOL": True
                },
                "CategoryName": {
                    "S": "Relational Database Service (MySQL)"
                },
                "CreatedAt": {
                    "N": "1642664593"
                },
                "CreationDate": {
                    "S": "2021-07-19T14:08:32 +0000"
                },
                "ExpiredAt": {
                    "N": "1657182739"
                },
                "FirstOutboundDate": {
                    "S": "None"
                },
                "FollowUps": {
                    "S": "[]"
                },
                "IsActionable": {
                    "BOOL": False
                },
                "IsActive": {
                    "BOOL": False
                },
                "IsFR": {
                    "BOOL": False
                },
                "LastInboundDate": {
                    "S": "2021-07-19T14:08:32 +0000"
                },
                "LastOutboundDate": {
                    "S": "None"
                },
                "Link": {
                    "S": "https://paragon-fe.amazon.com/hz/view-case?ie=UTF8&caseId=2229324583"
                },
                "MyLang": {
                    "S": "jp"
                },
                "NextResponseExpirationDate": {
                    "S": "2021-07-23T14:08:33 +0000"
                },
                "Owner": {
                    "S": "None"
                },
                "Plan": {
                    "S": "B"
                },
                "Profile": {
                    "S": "database"
                },
                "Queue": {
                    "S": "aws-support-tier2-database@amazon.co.jp"
                },
                "ResolutionDate": {
                    "S": "None"
                },
                "ResponseSLAMinutes": {
                    "N": "720"
                },
                "ResponseSLAStartDate": {
                    "S": "2021-07-19T14:08:33 +0000"
                },
                "Severity": {
                    "S": "B3"
                },
                "SLAExpirationDate": {
                    "S": "2021-07-20T02:09:33 +0000"
                },
                "SLARemaining": {
                    "S": "'-464057"
                },
                "StartDate": {
                    "S": "2021-07-19T14:08:33 +0000"
                },
                "Status": {
                    "S": "RES"
                },
                "StatusSLAExpirationDate": {
                    "S": "2021-07-23T14:08:33 +0000"
                },
                "Tags": {
                    "S": "[]"
                },
                "TypeName": {
                    "S": "General Guidance"
                }
                }
            
        )


        print(response)


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(main, [1, 2, 3, 4, 5]))
