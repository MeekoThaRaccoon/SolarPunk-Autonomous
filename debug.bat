# WRONG:
try: import flask; print('flask: OK'); except: print('flask: MISSING')

# CORRECT:
try: 
    import flask
    print('flask: OK')
except ImportError:
    print('flask: MISSING')