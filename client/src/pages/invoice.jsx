import { useParams } from "react-router-dom";

export default function Invoice() {
    let { invoiceId } = useParams();
    // let invoice = useFakeFetch(`/api/invoices/${invoiceId}`);
    let invoice = {'abalo':invoiceId}
    return invoice ? (
      <div>
        <h1>{invoice.abalo}</h1>
      </div>
    ) : (
        // <div>teste</div>
      <Loading />
    );
  }