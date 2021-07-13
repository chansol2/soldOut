import classes from "./Logout.module.css";
import { useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../../../store/auth-context";

const Logout = () => {
  const history = useHistory();
  const authCtx = useContext(AuthContext);
  const logoutHandler = (e) => {
    e.preventDefault();
    authCtx.logout();
    history.replace("/auth");
  };
  return (
    <div className={classes.container}>
      <button onClick={logoutHandler}>Log out</button>
    </div>
  );
};

export default Logout;
