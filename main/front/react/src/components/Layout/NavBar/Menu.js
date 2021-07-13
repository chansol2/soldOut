import { NavLink } from "react-router-dom";
import classes from "./Menu.module.css";


const Menu = () => {
  return (
    <div className={classes.container}>
      <NavLink activeClassName={classes.active} to="/dashboard">Dashboard</NavLink>
      <NavLink activeClassName={classes.active} to="/update">Update</NavLink>
      <NavLink activeClassName={classes.active} to="/upload">Upload</NavLink>
      <NavLink activeClassName={classes.active} to="/delete">Delete</NavLink>
      <NavLink activeClassName={classes.active} to="/rcmd">Recommend</NavLink>
    </div>
  );
};

export default Menu;
