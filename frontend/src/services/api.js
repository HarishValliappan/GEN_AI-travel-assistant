import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/api', // Update with your backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  getRecommendations(params) {
    return apiClient.post('/recommendations', params);
  },
  // Add more API methods as needed
};
