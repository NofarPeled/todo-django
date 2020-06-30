import httpService from './httpService';
import localStorageService from './localStorageService';
import types from './types';

export default {
    query,
    signIn,
    signUp,
    signOut 
}

async function query() {
    try {
        const token = localStorageService.load(types.TOKEN_API);
        if (!token) return null;
        const user = await httpService.get(`${types.TOKEN_API}/user/`, token);
        return user;
    } catch(err) {
        throw err;
    };
};

async function signIn(userCred) {
    try {   
        const { user, token } = await httpService.post(`${types.AUTH_API}/sign_in/`, userCred);
        localStorageService.save(types.TOKEN_API, token)
        return user;
    } catch(err) {
        throw err;
    };
};

async function signUp(userCred) {
    try {
        const { user, token }  = await httpService.post(`${types.AUTH_API}/sign_up/`, userCred);        
        localStorageService.save(types.TOKEN_API, token);
        return user;
    } catch(err) {
        throw err;
    };
};

async function signOut() {
    localStorageService.remove(types.TOKEN_API);
}