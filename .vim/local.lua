local group_name = 'LspAutoformat'
vim.api.nvim_create_augroup(group_name, {clear = true})
vim.api.nvim_create_autocmd('BufWritePre', {
    buffer = 0,
    callback = function() vim.lsp.buf.format({timeout_ms = 5000}) end,
    group = group_name
})

local function dap_python(config)
    return vim.tbl_extend('force', {
        type = 'python',
        request = 'launch',
        console = 'externalTerminal',
        pythonPath = os.getenv('VIRTUAL_ENV') .. '/bin/python'
    }, config)
end
require('dap').configurations.python = {
    dap_python({
        name = 'Launch current',
        program = '${file}' -- current file
    }), dap_python({
        name = 'Test current',
        code = 'import pytest; pytest.main(["${file}"])'
    })
}
