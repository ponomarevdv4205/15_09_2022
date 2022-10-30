import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import ProjectList from "./components/Project";
import axios from 'axios';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import ProjectsUsers from "./components/ProjectsUsers";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
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
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users'/>}/>
                        <Route path='/users'> # Передача Проектов конкретного Юзера
                            <Route index element={<UserList users={this.state.users}/>}/>
                            <Route path=':userId' element={<ProjectsUsers projects={this.state.projects}/>}/>
                        </Route> # Конец передачи Проектов конкретного Юзера

                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path='*' element={<NotFound404/>}/>

                    </Routes>
                </BrowserRouter>
            </div>
        )
    }


}


export default App;
