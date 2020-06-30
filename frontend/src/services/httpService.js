import axios from 'axios';

const BASE_URL =
  process.env.NODE_ENV === 'production'
    ? '/api/'
    : 'http://127.0.0.1:8000/api/';

axios.defaults.withCredentials = true;

async function ajax(endpoint, method = 'get', data = null, query = null) {
  try {
    const res = await axios({
      url: BASE_URL + endpoint,
      method,
      data,
      params: query
    });
    return res.data;
  } catch (err) {
    if (err.response && err.response.status === 401) {
      throw err.response.status;
    }
    
    throw err.response ? err.response.data.error : err;
  };
};

export default {
  get(endpoint, data, query) {
    return ajax(endpoint, 'GET', data, query);
  },
  post(endpoint, data) {
    return ajax(endpoint, 'POST', data);
  },
  put(endpoint, data) {
    return ajax(endpoint, 'PUT', data);
  },
  delete(endpoint, data) {
    return ajax(endpoint, 'DELETE', data);
  }
};
