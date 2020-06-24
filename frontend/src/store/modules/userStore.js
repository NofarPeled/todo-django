import userService from '../../services/userService';

export default({
    strict: true,
    state: {
        user: null
    },
    mutations: {
        setUser(state, { user }) {
            state.user = user;
        }
    },
    actions: {
        async signIn({ commit }, { userCred }) {
            const user = await userService.signIn(userCred);
            commit({ type: 'setUser', user });
        }, 
        async signUp({ commit }, { userCred }) {
            const user = await userService.signUp(userCred);
            commit({ type: 'setUser', user });
        },
        signOut({ commit }) {
            userService.signOut();
            commit({ type: 'setUser', user: null });
        }

    },
    getters: {
        user: state => state.user,
    }
});