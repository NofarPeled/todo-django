import todoService from '../../services/todoService';

export default({
    strict: true,
    state: {
        todos: [],
        todo: null,
        filterBy: {
            txt: ''
        },
        sortBy: {
            order: 1,
            key: 'createdAt'
        }
    },
    mutations: {
        setTodos(state, { todos }) {
            state.todos = todos;
        },
        setTodo(state, { todo }) {
            state.todo = todo;
        },
        addTodo(state, { todo }) {
            state.todos.push(todo);
        },
        updateTodo(state, { todo }) {
            state.todos.map(currTodo => {
                if (currTodo._id === todo._id) return todo;
                return currTodo;
            });
        },
        removeTodo(state, { id }) {
            state.todos.filter( todo => {
                return todo._id !== id;
            });
        }
    },
    actions: {
        async loadTodos({ commit, state }) {
            try {
                const todos = await todoService.query(state.filterBy);
                commit({ type: 'setTodos', todos });
            } catch (err) {
                throw err;
            }
        },
        async getTodoById({ commit }, { id }) {
            try {
                const todo = await todoService.getById(id);
                commit({ type: 'setTodo', todo });
            } catch (err) {
                throw err;
            }
        },
        async addTodo({ commit }, { todo }) {
            try {
                const updatedTodo = await todoService.add(todo);
                commit({ type: 'addTodo', updatedTodo });
            } catch (err) {
                throw err;
            }
        },
        async updateTodo({ commit }, { todo }) {
            try {
                const updatedTodo = await todoService.update(todo);
                commit({ type: 'updateTodo', updatedTodo });
            } catch (err) {
                throw err;
            }
        }, 
        async removeTodo({ commit }, { id }) {
            try {
                await todoService.remove(id);
                commit({ type: 'removeTodo', id });
            } catch (err) {
                throw err;
            }
        }
    },
    getters: {
        todos: state => state.todos,
        todo: state => state.todo,
        filterBy: state => state.filterBy,
        sortBy: state => state.sortBy
    }
});