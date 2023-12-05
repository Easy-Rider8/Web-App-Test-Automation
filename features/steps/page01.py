from behave import then


@then('the "{graph}" is loaded')

def validate_graph_loaded(context,graph):
    try:
        context.customPage.validateGraphLoad(graph)
    except:
        context.driver.close()
        assert False,"Test is failed in validating " + graph
