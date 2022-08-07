class Requests():
    new_requests = []
    requests_made = 0

    def __init__(self, user, date, timeslot, status='open'):
        self.user = user
        self.date = date
        self.timeslot = timeslot
        self.status = status

        Requests.requests_made += 1

    @property
    def info(self):
        return [self.user, self.date, self.timeslot, self.status]

    def add_request(self):
        for item in self.info:
            Requests.new_requests.append(item)

    def review_request(self, choice):
        if self.status == 'pending':
            if choice == 'accept':
                self.status = 'accepted'
            else:
                self.status = 'declined'
            
req_1 = Requests('Jill', '92/99/90', [1-2, 3-6], 'pending')
req_1.add_request()
print(Requests.new_requests)
print(Requests.requests_made)
req_1.review_request('')
print(req_1.status)