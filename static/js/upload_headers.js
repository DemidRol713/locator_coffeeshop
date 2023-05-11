self.addEventListener('fetch', function (event) {
    event.respondWith(async function () {
        let headers = new Headers()
        headers.append("Authorization", "Bearer {{access_token}}")
        return fetch(event.request, {headers: headers})
    }());
});