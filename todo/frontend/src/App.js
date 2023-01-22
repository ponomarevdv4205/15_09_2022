import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from './components/Users';
import NotFound404 from './components/NotFound404';
import ProjectList from './components/Project';
import UserProjects from './components/UserProjects';
import TodoProject from './components/Todos';
import TodoList from './components/Todos';
import LoginForm from './components/Auth';
import Footer from './components/Footer';
import ProjectForm from './components/ProjectForm';
import ToDoForm from './components/ToDoForm';
import axios from 'axios';
import Cookies from 'universal-cookie';
import { BrowserRouter, Route, Routes, Link, Navigate, Switch, Redirect } from "react-router-dom"

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': [],
        }
    }


    delete_project(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers})
            .then(response => {
                this.load_data()
            })
            .catch(error => {
                console.log(error)
                this.setState({projects: []})
        })
    }

    delete_todo(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
            .then(response => {
               this.load.data()
            }).catch(error => {
            this.setState({todos:[]})
        })
    }

    create_project(name, users){
        const headers = this.get_headers()
        const data = {name: name, users: users}
        axios.post(`http://127.0.0.1:8000/api/projects/`,data, {headers})
            .then(response => {
               this.load.data()
            }).catch(error => {
            this.setState({projects:[]})
        })
    }

    create_todo(text, user, project){
        const headers = this.get_headers()
        const data = {text: text, user: user, project: project}
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
             .then(response => {
               this.load.data()
             }).catch(error => {
            this.setState({todos:[]})
        })
    }

    get_token(username, password) {
        const data = { username: username, password: password }
        axios.post('http://127.0.0.1:8000/api/token/', data).then(response => {
            this.set_token(response.data['access'], username)
        }).catch(error => alert('Invalid login or password'))
    }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('username', username)
        console.log(cookies);
        this.setState({ 'token': token }, () => this.load_data())
        this.setState({ 'username': username })

    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({ 'token': token }, () => this.load_data())
    }

    is_auth() {

        return !!this.state.token, this.state.username
    }

    logout() {
        this.set_token('')
        this.setState({ 'users': [] }, () => this.load_data())
        this.setState({ 'projects': [] }, () => this.load_data())
        this.setState({ 'todos': [] }, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        };

        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

     load_data(){
         const headers = this.get_headers()

         axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))

         axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))

           axios
            .get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {
       this.get_token_from_storage()
    }


    render() {
        return (
            <div>
                {this.is_auth() ? <div>{this.state.username}<br /><button onClick={() => this.logout()}>Logout</button></div> : <LoginForm get_token={(username, password) => this.get_token(username, password)} />}
                <BrowserRouter>
                    <nav>
                    <div class="top">
                    <div class="container top__box">
                    <div class="top__info">
                    <h1 class="zag__level__1">Web-сервис для работы с ToDo-заметками</h1>
                        <p class="text">
                            Учебный проект на базе Django REST framework
                        </p>

                        <ul class="menu-bar">
                        <li>
                            <Link to='/'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todos'>Todos</Link>
                        </li>
                        </ul>

                        </div>
                        </div>
                        </div>

                    </nav>

                    <Routes>

                        <Route exect path='/' element={<Navigate to='/users' />} />
                        <Route path='/users'>
                            <Route index element={<UserList users={this.state.users} />} />
                            <Route path=':userId' element={<UserProjects projects={this.state.projects} />} />
                        </Route>

                        <Route path='/projects'>
                            <Route index element = {<ProjectList projects={this.state.projects} users={this.state.users} delete_project={(id)=>this.delete_project(id)}/>} />
                            <Route path='/projects/create' element={<ProjectForm users={this.state.users} create_project={(name, users) => this.create_project(name, users)}/>} />
                            <Route path=':projectId' element={<TodoProject todos={this.state.todos} />} />
                        </Route>

                        <Route exact path='/todos' element={
                            <TodoList todos={this.state.todos} delete_todo={(id) => this.delete_todo(id)}/>} />
                            <Route exact path='/todos/create' element={
                            <ToDoForm projects={(this.state.projects)} users={this.state.users} create_todo={(text, user, project) => this.create_todo(text, user, project)}/>} />

                        <Route path='*' element={<NotFound404 />} />
                        <Route path="/projects2" element={<Navigate replace to="/projects" />} />
                    </Routes>

                </BrowserRouter>

                <Footer />
            </div>
        )
    }

}

export default App;
