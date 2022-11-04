import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import UserProjects from './components/UserProjects';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import ProjectList from "./components/Project";
import axios from 'axios';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import ProjectsUsers from "./components/ProjectsUsers";
import TodoProject from './components/Todos';
import TodoList from './components/Todos';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
//            'tabs': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data
                    this.setState(
                    {
                        'projects': projects
                    }
                )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const todos = response.data
                    this.setState(
                    {
                        'todos': todos
                    }
                )
        }).catch(error => console.log(error))

//        const tabs = [{
//            'user': 'user',
//            'project': 'project',
//            'todo': 'todo'
//        }]
//        this.setState({ 'tabs': tabs })
//
    }

//    render () {
//        return (
//            <div>
//                <Menu />
//
//                <div class="div__right container">
//                    <div class="what-we-do container">
//                        <h3 class="h3">Список пользователей:</h3>
//                        <div class="elements">
//                            <UserList users={this.state.users} />
//                        </div>
//                    </div>
//                </div>
//
//                <Footer />
//            </div>
//        )
//    }

    render () {
        return (
            <div>
                <BrowserRouter>

                    <nav>
                        <li>
                            <Link to='/'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todos'>ToDos</Link>
                        </li>
                    </nav>

                    <Routes>

                        <Route exect path='/' element={<Navigate to='/users' />} />
                        <Route path='/users'>
                            <Route index element={<UserList users={this.state.users} />} />
                            <Route path=':userId' element={<UserProjects projects={this.state.projects} />} />
                        </Route>

                        <Route path='/projects'>
                            <Route index element={<ProjectList projects={this.state.projects} />} />
                            <Route path=':projectId' element={<TodoProject todos={this.state.todos} />} />
                        </Route>

                        <Route path='/todos' element={<TodoList todos={this.state.todos} />} />

                        <Route path='*' element={<NotFound404 />} />

                    </Routes>
                </BrowserRouter>
            </div>
        )
    }


}


export default App;
