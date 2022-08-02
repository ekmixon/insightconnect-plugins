from .scan_results import ScanResults


# Return the first element of an array, otherwise None.
def first(array):
    return next(iter(array or []), None)


# Generates correct payload that can be sent to Firepower
def generate_payload(results, operation, max_page_size):
    scan_results = ScanResults(max_page_size)

    for result in results:
        host = result.get("host", {})
        if ip_address := host.get("ip_address", ""):
            scan_results.add_scan_result(ip_address, result, operation)

        else:
            raise Exception("No IP address provided.")
    return scan_results.commands
