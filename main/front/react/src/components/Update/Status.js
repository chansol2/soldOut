import classes from "./Status.module.css";

const Status = (props) => {

  return (
    <div>
      {props.isLoading && <h1>is loading...</h1>}
      {!props.isLoading && (
        <div className={classes.container}>
          <div className={classes.cardOne}>
            <div className={classes.upper}>
              <div>
                <img alt="" />
              </div>
              <div>
                <div>2021.06.17.09:00시</div>
                <div>상품 업데이트를 완료했습니다.</div>
              </div>
            </div>
            <div className={classes.lower}>상품 업데이트 확인판</div>
          </div>
          <div className={classes.cardTwo}>
            <div className={classes.upper}>
              <strong>{props.loadedNumb}</strong>개 상품 수정 필요
            </div>
            <div className={classes.lower}>수정 필요 확인판</div>
          </div>
          <div className={classes.buttonContainer}>
            <div>
              <button onClick={props.onClickUpdate}>
                <img alt="" />
              </button>
              <div className={classes.text}>업데이트</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Status;
