import classes from "./NavigationBar.module.css";

import Profile from "./Profile";
import Menu from "./Menu";
import Logout from "./Logout";

const NavigationBar = () => {
  return (
    <div className={classes.container}>
      <Profile />
      <Menu />
      <Logout />
    </div>
  );
};

export default NavigationBar;
