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

async function query() {
    try {
        return await httpService.get(`${types.TODO_API}/`);
    } catch (err) {
        throw err;
    };
};

async function getById(id) {
    try {  
        return await httpService.get(`${types.TODO_API}/${id}`);
    } catch (err) {
        throw err;
    };
};

async function add(todo) {
    try {   
        return await httpService.post(`${types.TODO_API}/`, todo);
    } catch (err) {
        throw err;
    };
};

async function update(todo) {
    try {
        return await httpService.put(`${types.TODO_API}/${todo._id}/`, todo);
    } catch (err) {
        throw err;
    };
};

async function remove(id) {
    try {
        await httpService.delete(`${types.TODO_API}/${id}`);
    } catch (err) {
        throw err;
    };
};

