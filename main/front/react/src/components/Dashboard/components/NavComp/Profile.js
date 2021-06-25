import classes from "./Profile.module.css";

const Profile = () => {
  return (
    <div className={classes.container}>
      <div className={classes.subContainer}>
        <img alt="" />
      </div>
      <div className={classes.text}>레지스탕스 화이팅!</div>
    </div>
  );
};

export default Profile;
