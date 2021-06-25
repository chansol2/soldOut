import classes from "./DBLayout.module.css";

const DBLayout = (props) => {
  return <div className={classes.container}>{props.children}</div>;
};

export default DBLayout;
