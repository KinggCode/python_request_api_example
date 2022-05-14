import requests 

# GET HTTP Request
# api_url = 'https://jsonplaceholder.typicode.com/todos'
# response = requests.get(api_url)
# status = response.status_code
# print(response.headers['Content-Type'])
# print(response.json())

class RestAPIExample:
    def __init__(self,url):
        self.url = url

    def get_response(self):
        response = requests.get(self.url)
        return response 

    # Helper methods 
    def get_records(self,response):
        return response.json()

    def get_headers(self,response):
        return response.headers['Content-Type']

    def get_status_code(self,response):
        return response.status_code


    def post_record(self,data):
        response = requests.post(self.url,json=data)
        print(self.get_records(response))
        print(self.get_headers(response))
        print(self.get_status_code(response))
        print()

    def full_update_record(self,index,data):
        api_url =  self.url + "/" + str(index)

        response = requests.get(api_url)
        print(self.get_records(response))
        print(self.get_headers(response))
        print(self.get_status_code(response))
        print()

        response = requests.put(api_url, json=data)
        print('Full Updated Existing Resource')
        print(self.get_records(response))
        print(self.get_headers(response))
        print(self.get_status_code(response))
        print()

        # response.status_code
    def partial_update_record(self,index,data):
        api_url =  self.url + "/" + str(index)

        response = requests.get(api_url)
        print(self.get_records(response))
        print(self.get_headers(response))
        print(self.get_status_code(response))
        print()

        response = requests.patch(api_url,json=data)
        print('Partial Update Existing Resource')
        print(self.get_records(response))
        print(self.get_headers(response))
        print(self.get_status_code(response))
        print()

    def remove_record(self,index):
        api_url =  self.url + "/" + str(index)

        response = requests.delete(api_url)
        print(self.get_records(response))
        print(self.get_headers(response))
        print(self.get_status_code(response))
        print()





    
# Edge Cases:

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/todos'
    myapp = RestAPIExample(api_url)

    get_response = myapp.get_response()

    # Headers
    print('Request Header: ',myapp.get_headers(get_response))
    print('Status Code: ',myapp.get_status_code(get_response))
    print()

    # print('GET Output: ',myapp.get_records(get_response))

    print('POST Output: ')
    todo = {'userId':1,"title":"Buy Milk","completed":False}
    myapp.post_record(todo)

    print('PUT Output: ')
    todo = {'userId': 1, "title": "Wash Car", "completed": True}
    myapp.full_update_record(index=10,data=todo)

    print('PATCH Output: ')
    todo = {'title':'Mow lawn'}
    myapp.partial_update_record(10,todo)

    print('DELETE Output: ')
    myapp.remove_record(10)






    # print(get_response)