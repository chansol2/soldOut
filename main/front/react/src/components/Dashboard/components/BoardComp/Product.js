import classes from "./Product.module.css";

const Product = (props) => {
  return (
    <div className={classes.container}>
      <div className={classes.upper}>
        <div>상품 ID</div>
        <div>{props.prd.prd_id}</div>
      </div>
      <div className={classes.lower}>
        <div className={classes.item}>
          <div className={classes.key}>상품명</div>
          <div className={classes.value}>{props.prd["prd_nm"]}</div>
        </div>
        <div className={classes.item}>
          <div className={classes.key}>URL</div>
          <div className={classes.value}>{props.prd["org_url"]}</div>
        </div>
        <div className={classes.item}>
          <div className={classes.key}>가격</div>
          <div className={classes.value}>{props.prd["sales_price"]}</div>
        </div>
        <div className={classes.item}>
          <div className={classes.key}>품절상태</div>
          <div className={classes.value}>
            {props.prd["has_stock"] === false && "품절"}
            {props.prd["has_stock"] === undefined && "재고있음"}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Product;
