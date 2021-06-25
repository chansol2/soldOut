import classes from "./Board.module.css";
import Status from "./components/BoardComp/Status";

const Board = () => {
  return (
    <div className={classes.container}>
      <Status />
    </div>
  );
};

export default Board;
