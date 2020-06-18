import httpService from './httpService';

export default {
    query, 
    getById,
    add, 
    update, 
    remove
};

const TODO_API = 'todo'

async function query() {
    try {
        return await httpService.get(`${TODO_API}/`);
    } catch (err) {
        throw err;
    };
};

async function getById(id) {
    try {  
        return await httpService.get(`${TODO_API}/${id}`);
    } catch (err) {
        throw err;
    };
};

async function add(todo) {
    try {   
        console.log(todo, `${TODO_API}/`);
        
        return await httpService.post(`${TODO_API}/`, todo);
    } catch (err) {
        throw err;
    };
};

async function update(todo) {
    try {
        return await httpService.put(`${TODO_API}/${todo._id}/`, todo);
    } catch (err) {
        throw err;
    };
};

async function remove(id) {
    try {
        await httpService.delete(`${TODO_API}/${id}`);
    } catch (err) {
        throw err;
    };
};