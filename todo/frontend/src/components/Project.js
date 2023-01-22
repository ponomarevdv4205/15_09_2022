import React from "react";
import './Styles.css';
import {Link} from 'react-router-dom';


const ProjectItem =({project, delete_project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td><button onClick={()=>delete_project(project.id)}type='button'>Удалить</button></td>
        </tr>
    )
}

const ProjectList= ({projects, delete_project}) => {
    return(
        <div>
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Users ID</th>
            <th>Действие</th>
            {projects.map((project) => <ProjectItem project={project} delete_project={delete_project}/>)}
        </table>
        <br></br>
        <Link to='/projects/create'>Создать Проект</Link>
        </div>
    )
}

export default ProjectList
