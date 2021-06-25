import classes from "./Logout.module.css";
import { useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../../../../store/auth-context";

const Logout = () => {
  const history = useHistory();
  const authCtx = useContext(AuthContext);
  const logoutHandler = (e) => {
    e.preventDefault();
    console.log(authCtx.isLoggedIn);
    authCtx.logout();
    console.log(authCtx.isLoggedIn);

    history.replace("/");
  };
  return (
    <div className={classes.container}>
      <button onClick={logoutHandler}>Log out</button>
    </div>
  );
};

export default Logout;
