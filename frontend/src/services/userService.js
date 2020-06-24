import httpService from './httpService';
import localStorageService from './localStorageService';

export default {
    query,
    signIn,
    signUp,
    signOut 
}

const USER_API = 'user';
const TOKEN_API = 'token';

async function query() {
    try {
        const oldToken = localStorageService.load(TOKEN_API);
        if (!oldToken) return null;
        const { user, token } = await httpService.get(`${TOKEN_API}/`, oldToken);
        localStorageService.save(TOKEN_API, token);
        return user;
    } catch(err) {
        throw err;
    };
};

async function signIn(userCred) {
    try {   
        const { user, token } = await httpService.post(`${USER_API}/sign_in/`, userCred);
        localStorageService.save(TOKEN_API, token)
        return user;
    } catch(err) {
        throw err;
    };
};

async function signUp(userCred) {
    try {
        const { user, token } = await httpService.post(`${USER_API}/sign_up/`, userCred);
        localStorageService.save(TOKEN_API, token);
        return user;
    } catch(err) {
        throw err;
    };
};

async function signOut() {
    localStorageService.remove(TOKEN_API);
}

