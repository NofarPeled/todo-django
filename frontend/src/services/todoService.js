import httpService from './httpService';
import types from './types';
import localStorageService from './localStorageService';

export default {
    query, 
    getById,
    add, 
    update, 
    remove
};

const config = {
    headers: {}
}

async function query() {
    try {
        return await httpService.get(`${types.TODO_API}/`, null, _getConfig());
    } catch (err) {
        throw err;
    };
};

async function getById(id) {
    try {  
        return await httpService.get(`${types.TODO_API}/${id}`,null, _getConfig());
    } catch (err) {
        throw err;
    };
};

async function add(todo) {
    try {   
        return await httpService.post(`${types.TODO_API}/`, todo, _getConfig());
    } catch (err) {
        throw err;
    };
};

async function update(todo) {
    try {
        return await httpService.put(`${types.TODO_API}/${todo._id}/`, todo, _getConfig());
    } catch (err) {
        throw err;
    };
};

async function remove(id) {
    try {
        await httpService.delete(`${types.TODO_API}/${id}`,null, _getConfig());
    } catch (err) {
        throw err;
    };
};

function _getConfig(){
    const token = localStorageService.load(types.TOKEN_API)
    if (token) config.headers.Authorization = `Token ${token}`
    return config;
}
