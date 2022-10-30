import React from "react";
import './Styles.css';

const ProjectItem =({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectList= ({projects}) => {
    return(
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Users</th>
            {projects.map((project_) => <ProjectItem project={project_}/>)}
        </table>
    )
}

export default ProjectList
