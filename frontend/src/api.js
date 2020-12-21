import axios from 'axios';

class DepensesApi {
    constructor() {
        this.apiUrl = 'http://127.0.0.1:8000/api/v1/'
    }

    getToken() {
        return window.localStorage.getItem('x-auth-token')
    }

    makeEndpointUrl(endpoint) {
        return `${this.apiUrl}${endpoint}/`
    }

    async makeRoomMemberGetRequest(endpoint) {
        const response = await axios.get(`${this.apiUrl}${endpoint}`,
            {
                headers: {
                    Authorization: `Token ${this.getToken()}`
                }
            });
        return response;
    }


    async makeRoomMemberPostRequest(endpoint, data) {
        const response = await axios.post(this.makeEndpointUrl(endpoint), data,
            {
                headers: {
                    Authorization: `Token ${this.getToken()}`
                }
            });
        return response;
    }


    async makeRoomEndpointRequest(endpoint, roomId) {
        const response = await axios.get(`${this.apiUrl}room/${roomId}/${endpoint}/`,
            {
                headers: {
                    Authorization: `Token ${this.getToken()}`
                }
            });
        return response;
    }

    async makeApiPostRequest(endpoint, data) {
        const response = axios.post(this.makeEndpointUrl(endpoint), data,
            {
                headers: {
                    Authorization: `Token ${this.getToken()}`
                }
            }
        )
        return response;
    }


}
export default DepensesApi
