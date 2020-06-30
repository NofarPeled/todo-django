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
        async signIn({ commit }, { user }) {
            const updatedUser = await userService.signIn(user);
            commit({ type: 'setUser', user : updatedUser });
        }, 
        async signUp({ commit }, { user }) {
            const updatedUser = await userService.signUp(user);
            commit({ type: 'setUser', user : updatedUser });
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