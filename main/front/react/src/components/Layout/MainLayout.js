import { Fragment } from 'react';

import classes from "./MainLayout.module.css";
import NavigationBar from './NavBar/NavigationBar';

const MainLayout = (props) => {
  return (
    <div className={classes.container}>
      <NavigationBar/>
      <Fragment>{props.children}</Fragment>
    </div>
  );
};

export default MainLayout;
